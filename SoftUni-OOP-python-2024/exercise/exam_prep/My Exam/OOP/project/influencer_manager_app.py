from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPE = {"PremiumInfluencer": PremiumInfluencer,  "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN_TYPE = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type, username, followers, engagement_rate):
        if influencer_type not in self.VALID_INFLUENCER_TYPE.keys():
            return f"{influencer_type} is not an allowed influencer type."
        try:
            influencer = next(filter(lambda i: i.username == username, self.influencers))
        except StopIteration:
            new_influencer = self.VALID_INFLUENCER_TYPE[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

        return f"{username} is already registered."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPE.keys():
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            new_campaign = self.VALID_CAMPAIGN_TYPE[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

        return f"Campaign ID {campaign_id} has already been created."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            check_influencer = next(filter(lambda x: x.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            check_campaign = next(filter(lambda x: x.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not check_campaign.check_eligibility(check_influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = check_influencer.calculate_payment(check_campaign)
        if payment > 0.0:
            check_campaign.approved_influencers.append(check_influencer)
            check_campaign.budget -= payment
            check_influencer.campaigns_participated.append(check_campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            total_followers = 0
            for influencer in campaign.approved_influencers:
                total_followers += influencer.reached_followers(influencer.__class__.__name__)
            if total_followers > 0:
                total_reached_followers[campaign] = total_followers
        return total_reached_followers

    def influencer_campaign_report(self, username):
        check_influencer = [x for x in self.influencers if x.username == username][0]

        if not check_influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return check_influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_capmaogns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        info = ""
        for campaign in sorted_capmaogns:
            total_reached_followers = sum(influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers)
            info += f"  * Brand: {campaign.brand}, " \
                    f"Total influencers: {len(campaign.approved_influencers)}," \
                    f" Total budget: ${campaign.budget:.2f}," \
                    f" Total reached followers: {total_reached_followers}\n"
        sorted_campaigns_info = f"$$ Campaign Statistics $$\n{info}"

        return sorted_campaigns_info
