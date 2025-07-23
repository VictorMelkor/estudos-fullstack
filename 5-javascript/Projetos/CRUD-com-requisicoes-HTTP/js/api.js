const api = {
    async buscarPensamentos() {
        try {
            const response = await fetch('http://localhost:3000/pensamentos');
            return await response.json()
        }
        catch {
            alert('Erro ao buscar pensamentos');
            throw error
        }
    }
}

export default api;