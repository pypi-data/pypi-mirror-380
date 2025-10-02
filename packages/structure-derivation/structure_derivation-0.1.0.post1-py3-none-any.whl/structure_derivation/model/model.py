import torch
import torch.nn as nn
from transformers import PreTrainedModel, PretrainedConfig
from structure_derivation.model.htsat import HTSAT_Swin_Transformer


class StructureDerivationModelConfig(PretrainedConfig):
    model_type = "structure-derivation"

    def __init__(self, spec_size=512, patch_size=4, patch_stride=(4,4), 
                in_chans=1, num_classes=1,
                 embed_dim=96, depths=[2, 2, 6, 2], num_heads=[4, 8, 16, 32], htsat_window_size=8,
                 window_size=1024, mlp_ratio=4., qkv_bias=True, qk_scale=None,
                 drop_rate=0., attn_drop_rate=0., drop_path_rate=0.1,
                 norm_layer="layernorm", ape=False, patch_norm=True, use_checkpoint=False, 
                 norm_before_mlp='ln', enable_tscam=True, sample_rate=32000, hop_size=320, mel_bins=128,
                 fmin=20, fmax=16000, htsat_attn_heatmap=False, htsat_hier_output=False,
                 htsat_use_max=False, enable_repeat_mode=False, loss_type=None, temperature=0.1, **kwargs):
        super().__init__(**kwargs)
        
        # model architecture
        self.spec_size = spec_size
        self.patch_stride = patch_stride
        self.patch_size = patch_size
        self.htsat_window_size = htsat_window_size
        self.window_size = window_size
        self.embed_dim = embed_dim
        self.depths = depths
        self.ape = ape
        self.in_chans = in_chans
        self.num_classes = num_classes
        self.num_heads = num_heads
        self.mlp_ratio = mlp_ratio
        self.qkv_bias = qkv_bias
        self.qk_scale = qk_scale
        self.drop_rate = drop_rate
        self.attn_drop_rate = attn_drop_rate
        self.drop_path_rate = drop_path_rate
        self.norm_layer = norm_layer
        self.patch_norm = patch_norm
        self.use_checkpoint = use_checkpoint
        self.norm_before_mlp = norm_before_mlp
        # for model's design
        self.enable_tscam = enable_tscam  # enable the token-semantic layer
        # for signal processing
        self.sample_rate = sample_rate
        self.htsat_window_size = htsat_window_size
        self.window_size = window_size
        self.hop_size = hop_size
        self.mel_bins = mel_bins
        self.fmin = fmin
        self.fmax = fmax
        # HTSAT specific
        self.htsat_attn_heatmap = htsat_attn_heatmap
        self.htsat_hier_output = htsat_hier_output
        self.htsat_use_max = htsat_use_max
        self.enable_repeat_mode = enable_repeat_mode
        self.loss_type = loss_type  # clip_ce
        # Contrastive learning specific
        self.temperature = temperature  # for NT-Xent loss


class StructureDerivationModel(PreTrainedModel):
    config_class = StructureDerivationModelConfig
    def __init__(self, config: StructureDerivationModelConfig):
        super().__init__(config)
        self.htsat = HTSAT_Swin_Transformer(config)
        self.temperature = config.temperature
        self.loss_fct = nn.CrossEntropyLoss()

    def nt_xent_loss(self, z1, z2):
        """
        Calculates the NT-Xent loss for contrastive learning.
        z1: (B, D) # embeddings for the first view
        z2: (B, D) # embeddings for the second view
        """
        # Normalize the embeddings
        z1 = nn.functional.normalize(z1, p=2, dim=1)
        z2 = nn.functional.normalize(z2, p=2, dim=1)

        # Cosine similarity matrix
        cos_sim = torch.matmul(z1, z2.T) / self.temperature
        
        # Create labels for the positive pairs (diagonal elements)
        batch_size = z1.shape[0]
        labels = torch.arange(batch_size, device=z1.device)

        # Calculate the loss
        loss = self.loss_fct(cos_sim, labels)
        return loss

    def forward(self, x1, x2=None, infer_mode=False):
        """
        x1: (B, T) # waveform input
        x2: (B, T) # optional, waveform input for contrastive learning
        infer_mode: bool, whether in inference mode
        return: Dictionary with loss and/or latent representations
        """
        if x2 is None:
            output = self.htsat(x1, infer_mode=infer_mode)
            return {
                'latent_output': output['latent_output']
            }
        else:
            output1 = self.htsat(x1, infer_mode=infer_mode)
            output2 = self.htsat(x2, infer_mode=infer_mode)
            
            z1 = output1['latent_output']
            z2 = output2['latent_output']
            
            loss = self.nt_xent_loss(z1, z2)
            
            return {
                'loss': loss,
                'latent_output1': z1,
                'latent_output2': z2
            }