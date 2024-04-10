from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, budget=self.BUDGET, required_engagement=required_engagement)

    def check_eligibility(self, engagement_rate: float):
        required_engagement = self.required_engagement
        return engagement_rate >= 0.9 * required_engagement
