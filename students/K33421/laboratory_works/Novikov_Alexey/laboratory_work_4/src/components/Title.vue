<script setup>
import {useAuthStore} from "@/stores";

const props = defineProps({
  groupName: String,
  showGroupName: Boolean,
  showTitle: Boolean,
  showLogout: Boolean,
})

const logout = async () => {
  const authStore = useAuthStore();

  return await authStore.logout()
};
</script>

<template>
  <v-btn v-if="showLogout" prepend-icon="mdi-exit-to-app" variant="text" class="exit-button" @click="logout">Выйти</v-btn>
  <div v-if="showTitle" class="container">
    <img src="../assets/images/sun.png" class="sun-image">
    <div class="centered">
      <span class="main">
        Опрос
      </span>
      <span class="extra">
        по работе адаптеров
      </span>
      <span class="extra" v-if="groupName && showGroupName">
        группы {{ groupName }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.container {
  position: relative;
  text-align: center;
}
.centered {
  position: absolute;
  width: 100%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 40%;
  min-height: 100px;
}
.sun-image {
  //width: 100%;
}
.main {
  display: block;
  color: #F1F1F1;
  font-size: 43px;
  font-family: 'Actay Wide';
  font-weight: 700;
  letter-spacing: 2.15px;
  word-wrap: break-word;
  margin-bottom: -10px;
  margin-top: -10px;
  text-shadow:
    0.7px 0.7px 0 #222222,
    -0.7px -0.7px 0 #222222,
    0.7px -0.7px 0 #222222,
    -0.7px 0.7px 0 #222222,
    0 2.5px 0 #222222;
}
.extra {
  display: block;
  color: #F1F1F1;
  font-size: 22px;
  font-family: 'Actay Wide';
  font-weight: 700;
  letter-spacing: 1.07px;
  word-wrap: break-word;
  text-shadow:
    0.7px 0.7px 0 #222222,
    -0.7px -0.7px 0 #222222,
    0.7px -0.7px 0 #222222,
    -0.7px 0.7px 0 #222222,
    0 2.5px 0 #222222;
}
.exit-button {
  z-index: 100;
  text-transform: none;
  font-family: "Actay Wide";
  position: absolute;
  right: 10px;
  top: 10px;
  border: none;
  font-size: 16px;
  padding: 10px;
  border-radius: 5px;
  display: flex;
}
</style>
