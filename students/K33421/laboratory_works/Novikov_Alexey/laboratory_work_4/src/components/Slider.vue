<script setup>
import {ref, watch, onMounted } from "vue"

import { Label } from "@/components";

const props = defineProps({
  id: String,
  text: String,
  helpText: String
})

const emit = defineEmits(['update:sliderValue'])

let sliderValue = ref(3)

watch(sliderValue, (newVal) => {
  emit('update:sliderValue', newVal)
})

onMounted(() => {
  emit('update:sliderValue', sliderValue.value)
})
</script>

<template>
  <Label :id="id" :text="text" :helpText="helpText" />
  <div class="slider-container">
    <span class="slider-number">1</span>
    <v-slider
      class="custom-slider"
      :id="id"
      track-color="#F1F1F1"
      :max="5" :min="1"
      :step="1"
      :thumb-label=true
      :hide-details=true
      v-model="sliderValue"
    />
    <span class="slider-number">5</span>
  </div>
</template>

<style scoped>
.slider-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.custom-slider {
  padding: 0 1em;
}
.slider-number {
  font-family: "Actay Wide";
}
</style>
