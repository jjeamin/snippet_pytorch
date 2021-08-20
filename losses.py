import torch
import torch.nn as nn


class FocalLoss(nn.Module):
    def __init__(self, gamma=2, alpha=0.5, ignore_index=255, device='cuda'):
        super().__init__()

        self.gamma = gamma
        self.alpha = alpha
        self.ignore_index = ignore_index
        self.criterion = nn.CrossEntropyLoss(ignore_index=ignore_index).to(device)
        
    def forward(self, logits, targets):
        """
        Args:
            logits (FloatTensor): preds (b, c, h, w) 
            targets (LongTensor): labels (b, 1, h, w)

        Returns:
            Tensor: loss value
        """
        logpt = self.criterion(logits, targets)
        # -log(pt)

        pt = torch.exp(-logpt)
        # -log(pt) -> log(pt) -> pt

        loss = self.alpha * ((1 - pt) ** self.gamma) * logpt
        # alpha * ((1 - pt) ** gamma) * -log(pt)

        return loss