<script setup>
import { ref, watch } from 'vue';

import { Label } from "@/components";

let textArea = ref("");

const props = defineProps({
  id: String,
  text: String,
  helpText: String,
})

const emit = defineEmits(['update:textArea']);

watch(textArea, (newVal) => {
  emit('update:textArea', newVal)
})
</script>

<template>
  <Label :id="id" :text="text" :helpText="helpText" />
  <v-textarea
    class="my-textarea"
    bg-color="#F1F1F1"
    :no-resize=true
    rows="5"
    maxlength="1000"
    v-model="textArea"
  />
  <div class="char-count">{{ textArea.length }} / 1000</div>
</template>

<style scoped>
.my-textarea:deep(.v-field__input) {
  font-family: "Actay Wide";
}
.my-textarea:deep(.v-input__details) {
  border-top: 3px solid black;
}
.char-count {
  text-align: right;
  font-family: "Actay Wide";
  padding: 0;
  margin: 0;
}
</style>
