<template>
  <div class="loading-screen">
    <img class="gif" src="@/assets/images/spinning_adapter.gif" alt="Загрузка..." />
    <p class="disclaimer">Обнуляем вашу стипендию...</p>
  </div>
</template>

<style>
.loading-screen {
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(100, 181, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.gif {
  height: 200px;
}
.disclaimer {
  font-family: "Actay Wide";
  font-size: 20px;
  text-align: center;
}
</style>
