<script setup>
const props = defineProps({
  id: String,
  text: String,
  helpText: String,
})
</script>

<template>
  <label :for="id" class="form-label" style="display: inline-block;">
    <span style="font-size: larger;">{{ text }}</span>
    <br>
    <span style="font-size: smaller;">{{ helpText }}</span>
  </label>
</template>

<style scoped>
.form-label {
  font-family: "Actay Wide";
}
</style>
