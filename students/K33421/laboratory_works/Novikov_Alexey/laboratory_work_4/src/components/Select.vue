<script setup>
import {ref, computed, watch} from 'vue';

import { Label } from "@/components";

const props = defineProps({
  id: String,
  text: String,
  helpText: String,
})

const emit = defineEmits(['selectedValue', 'error']);

let selectedValue = ref('');

watch(selectedValue, (newVal) => {
  emit('update:selectedValue', newVal)
})

const error = computed(() => !selectedValue.value);
watch(error, (newVal) => {
  emit('update:error', newVal);
});

</script>

<template>
  <Label :id="id" :text="text" :helpText="helpText" />
  <v-select
    v-model="selectedValue"
    :id="id"
    class="my-select"
    :class="{ 'has_error': error }"
    :items="['Да', 'Нет']"
    bg-color="#F1F1F1"
    :error="error"
    :error-messages="error ? 'Поле обязательно для заполнения!' : ''"
  />
</template>

<style scoped>
.my-select:deep(.v-input__details) {
  border-top: 3px solid black;
}
.has_error:deep(.v-input__details) {
  border-top: 3px solid red;
}
.my-select:deep(.v-select__selection-text) {
  font-family: "Actay Wide";
}
.my-select:deep(.v-overlay-container){
  font-family: "Actay Wide";
}
.my-select:deep(.v-messages__message) {
  font-family: "Actay Wide";
}
</style>

