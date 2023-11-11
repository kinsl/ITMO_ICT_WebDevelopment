<script setup>
import { ref, watch, onMounted } from "vue"

import { Label } from "@/components";

const props = defineProps({
  id: String,
  text: String,
  helpText: String,
  adapters: Array
})

const emit = defineEmits(['update:sliderValue'])

let sliderValues = ref({});

onMounted(() => {
  sliderValues.value = props.adapters.reduce((accumulator, adapter) => {
    accumulator[adapter.id] = 3;
    return accumulator;
  }, {})
})

watch(sliderValues, (newVal) => {
  emit('update:sliderValue', newVal);
}, { deep: true });


</script>

<template>
  <Label :id="id" :text="text" :helpText="helpText" />
  <div class="adapters" v-for="adapter in props.adapters">
    <label :for="`id_${adapter.id}`" class="form-label" style="display: inline-block;">
      <span style="font-size: smaller;">{{ adapter.full_name }}</span>
    </label>
    <div class="slider-container">
      <span class="slider-number">1</span>
      <v-slider
        class="custom-slider"
        :id="`id_${adapter.id}`"
        track-color="#F1F1F1"
        :max="5" :min="1"
        :step="1"
        :thumb-label="true"
        :hide-details="true"
        v-model="sliderValues[adapter.id]"
      />
      <span class="slider-number">5</span>
    </div>
  </div>
</template>

<style scoped>
.adapters {
  padding-top: 10px;
}
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
.form-label {
  font-family: "Actay Wide";
}
</style>
