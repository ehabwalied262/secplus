const API_BASE_URL = window.location.origin + '/api';

const API = {
    // User Endpoints
    async getQuestions(objective, limit = 10) {
        try {
            const response = await fetch(`${API_BASE_URL}/questions/?objective=${objective}&limit=${limit}`);
            if (!response.ok) throw new Error('Failed to fetch questions');
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            return [];
        }
    },

    // Admin Endpoints
    async getUnverifiedQuestions() {
        try {
            const response = await fetch(`${API_BASE_URL}/admin/unverified`);
            if (!response.ok) throw new Error('Failed to fetch unverified questions');
            return await response.json();
        } catch (error) {
            console.error('Admin API Error:', error);
            return [];
        }
    },

    async verifyQuestion(id, isVerified = true) {
        try {
            const response = await fetch(`${API_BASE_URL}/admin/${id}`, {
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ verified: isVerified })
            });
            return await response.json();
        } catch (error) {
            console.error('Verify Error:', error);
        }
    },

    async updateQuestion(id, updatedData) {
        try {
            const response = await fetch(`${API_BASE_URL}/admin/${id}`, {
                method: 'PATCH',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedData)
            });
            return await response.json();
        } catch (error) {
            console.error('Update Error:', error);
        }
    },

    async deleteQuestion(id) {
        try {
            const response = await fetch(`${API_BASE_URL}/admin/${id}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Delete Error:', error);
        }
    }
};

window.API = API;