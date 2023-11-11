<script setup>
import { onMounted, ref, watch } from "vue";
import { fetchWrapper } from "@/helpers";
import { Title, Footer, View } from "@/components";

const baseUrl = `${import.meta.env.VITE_API_URL}`;

const props = defineProps({
  showTitle: Boolean,
  showGroupName: Boolean,
  showLogout: Boolean,
});

const groupName = ref("")

const fetchData = async () => {
  if (props.showGroupName && props.showTitle) {
    try {
      const data = await fetchWrapper.get(`${baseUrl}/oidc/group/`);
      if (data) {
        groupName.value = data.group;
      }
    } catch (err) {
      console.error(err);
    }
  }
};

onMounted(fetchData);

watch(() => props.showGroupName, fetchData);
</script>

<template>
  <v-app style="background-color: #64B5FF">
    <Title :group-name="groupName" :show-title="showTitle" :show-logout="showLogout" :show-group-name="showGroupName"/>
    <View />
    <Footer />
  </v-app>
</template>

<style scoped>

</style>
