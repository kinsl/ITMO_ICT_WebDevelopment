import { defineStore } from 'pinia';

import { fetchWrapper, router } from '@/helpers';

const baseUrl = `${import.meta.env.VITE_API_URL}`;

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    access: JSON.parse(localStorage.getItem('access')),
    access_expiration: JSON.parse(localStorage.getItem('access_expiration')),
    refresh: JSON.parse(localStorage.getItem('refresh')),
    refresh_expiration: JSON.parse(localStorage.getItem('refresh_expiration')),
  }),
  actions: {
    async login(code) {
      const data = await fetchWrapper.post(`${baseUrl}/oidc/login/`, { code });
      this.access = data.access;
      this.access_expiration = data.access_expiration;
      this.refresh = data.refresh;
      this.refresh_expiration = data.refresh_expiration;

      localStorage.setItem('access', JSON.stringify(data.access));
      localStorage.setItem('access_expiration', JSON.stringify(data.access_expiration));
      localStorage.setItem('refresh', JSON.stringify(data.refresh));
      localStorage.setItem('refresh_expiration', JSON.stringify(data.refresh_expiration));

      await router.push('/survey');
    },
    async logout() {
      this.access = null;
      this.access_expiration = null;
      this.refresh = null;
      this.refresh_expiration = null;

      localStorage.removeItem('access');
      localStorage.removeItem('access_expiration');
      localStorage.removeItem('refresh');
      localStorage.removeItem('refresh_expiration');

      await router.push('/login');
    },
    updateAccessToken(access, access_expiration) {
      this.access = access;
      this.access_expiration = access_expiration;

      localStorage.setItem('access', JSON.stringify(access));
      localStorage.setItem('access_expiration', JSON.stringify(access_expiration));
    }
  }
});
