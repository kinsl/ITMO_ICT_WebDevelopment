<script setup>
const props = defineProps({
  disabled: Boolean,
})
</script>

<template>
  <v-btn color="#F1F1F1" type="submit" :disabled="disabled">
    Отправить
  </v-btn>
</template>

<style scoped>
.v-btn {
  text-transform: none;
  font-size: 15px;
  font-family: "Actay Wide";
  border-radius: 20px;
  border: 3px solid #222222;
}
</style>
