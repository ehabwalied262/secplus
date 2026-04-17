from config import supabase

class QuestionService:
    @staticmethod
    def get_verified_questions(objective: str, limit: int = 15):
        """
        Fetches questions for a specific objective.
        Note: We are filtering by verified=True so the quiz stays high-quality.
        """
        response = supabase.table("questions") \
            .select("*") \
            .eq("domain_number", objective) \
            .eq("verified", True) \
            .limit(limit) \
            .execute()
        
        return response.data

    @staticmethod
    def get_unverified_questions():
        """Used by the Admin panel to show what needs review."""
        response = supabase.table("questions") \
            .select("*") \
            .eq("verified", False) \
            .execute()
        return response.data