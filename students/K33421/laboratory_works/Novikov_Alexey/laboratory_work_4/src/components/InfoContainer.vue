<script setup>
const props = defineProps({
  text: String
})
</script>

<template>
  <div class="container">
    {{ text }}
  </div>
</template>

<style scoped>
.container {
  width: 300px;
  font-size: 20px;
  text-align: center;
  background: #F1F1F1;
  font-family: "Actay Wide";
  border-radius: 10px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: inline-flex;
  align-items: center;
  border: 2px solid black;
  padding: 20px;
}
</style>
