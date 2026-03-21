from models.policy_user_map_model import PolicyAccount

class BalanceValidator:

    @staticmethod
    def validate(user_id, claimed_amount):
        account = PolicyAccount.query.filter_by(user_id=user_id).first()

        if not account:
            return False, "No policy account found"

        if account.remaining_amount < claimed_amount:
            return False, "Insufficient policy balance"

        return True, "Sufficient balance"