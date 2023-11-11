<script setup>
import{ ref, onMounted } from 'vue';

import { fetchWrapper } from '@/helpers';
import { useAuthStore } from '@/stores';
import { LoginButton, LoadingScreen } from "@/components";

const baseUrl = `${import.meta.env.VITE_API_URL}`;
const disabled = ref(false)

const authenticate = async () => {
  disabled.value = true;
  const response = await fetchWrapper.get(`${baseUrl}/oidc/auth/url/`);
  window.location.href = response.url;
};

onMounted(async () => {
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');

  if (code) {
    disabled.value = true;
    await login(code);
  }
});

const login = async (code) => {
  const authStore = useAuthStore();

  return authStore.login(code)
};
</script>

<template>
  <LoginButton @click="authenticate" :disabled="disabled"/>
  <LoadingScreen v-if="disabled" />
</template>

<style scoped>

</style>
