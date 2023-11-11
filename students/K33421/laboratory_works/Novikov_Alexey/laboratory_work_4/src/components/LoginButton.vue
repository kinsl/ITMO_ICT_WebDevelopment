<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  disabled: Boolean
});

const emits = defineEmits(['click']);
const handleClick = () => {
  if (!props.disabled) emits('click');
};
</script>
<template>
  <div class="button-container">
    <v-btn color="#F1F1F1" @click="handleClick" :disabled="props.disabled">
      Авторизоваться
    </v-btn>
    <p class="disclaimer">
      Опрос полностью анонимный, мы не собираем личную информацию (номер ИСУ, ФИО)
    </p>
  </div>
</template>
<style scoped>
.button-container {
  max-width: 450px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.v-btn {
  width: 90%;
  text-transform: none;
  font-size: 30px;
  font-family: "Actay Wide";
  border-radius: 20px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  padding: 40px 50px;
  border: 3px solid #222222;
}
.v-btn:deep(.v-btn__overlay) {
  border-radius: 17px;
}

.disclaimer {
  width: 90%;
  font-family: "Actay Wide";
  font-size: 14px;
  text-align: center;
}
</style>
