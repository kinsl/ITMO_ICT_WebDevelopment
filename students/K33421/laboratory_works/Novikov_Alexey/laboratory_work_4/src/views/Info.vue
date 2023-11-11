<script setup>
import {onMounted, ref} from 'vue'

import { useInfoStore } from '@/stores';
import { InfoContainer } from "@/components";

const text = ref("")

onMounted( () => {
    const infoStore = useInfoStore();
    if (!infoStore.text && localStorage.getItem('info_message')) {
      infoStore.setText(localStorage.getItem('info_message'));
    }
    text.value = infoStore.text
});
</script>

<template>
  <div class="image-container">
    <div class="bird2-container">
      <img src="@/assets/images/birds2.png">
    </div>
    <InfoContainer :text="text" />
    <div class="bird1-container">
      <img src="@/assets/images/birds.png">
    </div>
  </div>
</template>

<style scoped>
.image-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  max-width: 800px;
  height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url("@/assets/images/full-sun.png") no-repeat center center;
  background-size: auto;
}
.bird1-container {
  position: absolute;
  right: 0;
  bottom: 0;
  margin-right: 20px;
}
.bird2-container {
  position: absolute;
  top: 0;
  left: 0;
  margin-left: 20px;
}
</style>
