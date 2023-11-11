<script setup>
import {computed, ref, watch} from 'vue';

import { Select, Slider } from "@/components";

const props = defineProps({
  id: String,
  text: String,
  helpText: String,
  trainingText: String,
  trainingHelpText: String
})

const emit = defineEmits(['update:selectedValue', 'update:error']);

let selectedValue = ref('');
watch(selectedValue, (newVal) => {
  let emitValue = newVal === "Нет" ? 0 : sliderValue.value;
  emit('update:selectedValue', emitValue);
})

let sliderValue = ref('')
watch(sliderValue, (newVal) => {
  if (selectedValue.value === "Да"){
    emit('update:selectedValue', newVal);
  }
})

const error = computed(() => !selectedValue.value);
watch(error, (newVal) => {
  emit('update:error', newVal);
});

</script>

<template>
  <Select
    :id="id"
    :text="text"
    :helpText="helpText"
    @update:selectedValue="val => { selectedValue = val }"
    @update:error="val => { error = val }"
  />

  <Slider
    v-if="selectedValue === 'Да'"
    :id="id"
    :text="trainingText"
    :helpText="trainingHelpText"
    @update:sliderValue="val => { sliderValue = val }"
  />
</template>

<style scoped>

</style>
