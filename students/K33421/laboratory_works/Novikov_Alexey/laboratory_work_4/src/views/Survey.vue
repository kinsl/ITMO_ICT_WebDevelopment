<script setup>
import { ref, onMounted } from 'vue'

import { fetchWrapper, router } from '@/helpers';
import { useInfoStore } from '@/stores';

import { AdapterSlider, Select, Slider, SubmitButton, TextArea, TrainingSelect } from "@/components";

const baseUrl = `${import.meta.env.VITE_API_URL}`;
let isSending = ref(false);

const onSubmit = async () => {
  if (errors.value.length > 0) {
    return;
  }

  isSending.value = true;
  const info = useInfoStore();

  const formValuesList = Object.keys(formValues).map(key => {
    if (typeof formValues[key] === 'object' && formValues[key] !== null) {
      return {
        id: parseInt(key),
        value: Object.keys(formValues[key]).map(innerKey => ({
          id: parseInt(innerKey),
          value: formValues[key][innerKey]
        }))
      };
    }
    else {
      return {
        id: parseInt(key),
        value: formValues[key]
      };
    }
  });

  try {
    await fetchWrapper.post(`${baseUrl}/api/survey/answers/`, formValuesList);
    info.setText('Опрос пройден!\nСпасибо 💙');
  } catch (error) {
    info.setText('Произошла ошибка при сохранении ответов!');
  }
  await router.push('/info');
}

const formFields = ref([])
const formValues = {}
const errors = ref([])

onMounted(async () => {
  try {
    const data = await fetchWrapper.get(`${baseUrl}/api/survey/questions/`)
    if(data) {
      formFields.value = data
      data.forEach((field) => {
        formValues[field.id] = ''
        if (field.component === 'Select' || field.component === 'TrainingSelect') {
          errors.value.push(field.id)
        }
      })
    }
  } catch(err) {
    console.error(err)
  }
})
</script>

<template>
  <div class="form-container">
    <v-form @submit.prevent="onSubmit" class="form-content">
      <div class="field" v-for="(field, index) in formFields" :key="index">
        <TextArea
          v-if="field.component === 'TextArea'"
          :id="`${field.id}`"
          :text="field.text"
          :helpText="field.help_text"
          @update:textArea="val => {
            formValues[field.id] = val
          }"
        />
        <Select
          v-else-if="field.component === 'Select'"
          :id="`${field.id}`"
          :text="field.text"
          :helpText="field.help_text"
          @update:selectedValue="val => formValues[field.id] = val"
          @update:error="val => {
            if (val) {
              if (!errors.includes(field.id)) {
                errors.push(field.id)
              }
            } else {
              const index = errors.indexOf(field.id)
              if (index > -1) {
                errors.splice(index, 1)
              }
            }
          }"
        />
        <TrainingSelect
          v-else-if="field.component === 'TrainingSelect'"
          :id="`${field.id}`"
          :text="field.text"
          :helpText="field.help_text"
          :training-text="field.training_text"
          :training-help-text="field.training_help_text"
          @update:selectedValue="val => formValues[field.id] = val"
          @update:error="val => {
            if (val) {
              if (!errors.includes(field.id)) {
                errors.push(field.id)
              }
            } else {
              const index = errors.indexOf(field.id)
              if (index > -1) {
                errors.splice(index, 1)
              }
            }
          }"
        />
        <AdapterSlider
          v-else-if="field.component === 'AdapterSlider'"
          :id="`${field.id}`"
          :text="field.text"
          :helpText="field.help_text"
          :adapters="field.adapters"
          @update:sliderValue="val => formValues[field.id] = val"
        />
        <Slider
          v-else-if="field.component === 'Slider'"
          :id="`${field.id}`"
          :text="field.text"
          :helpText="field.help_text"
          @update:sliderValue="val => formValues[field.id] = val"
        />
      </div>
      <div class="center-button">
        <SubmitButton v-if="formFields.length>0" :disabled="errors.length>0 || isSending"/>
      </div>
    </v-form>
  </div>
</template>

<style scoped>
.form-container {
  display: flex;
  justify-content: center;
}
.form-content {
  padding-left: 20px;
  padding-right: 20px;
  max-width: 600px;
  width: 100%;
}
.center-button {
  display: flex;
  justify-content: center;
  padding-bottom: 30px;
}
.field {
  padding-top: 30px;
}
</style>
