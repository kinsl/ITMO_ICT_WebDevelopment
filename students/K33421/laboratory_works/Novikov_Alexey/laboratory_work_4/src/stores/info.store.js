import { defineStore } from 'pinia';

export const useInfoStore = defineStore({
  id: 'info',
  state: () => ({
    text: ''
  }),
  actions: {
    setText(message) {
      this.text = message;
      localStorage.setItem('info_message', message);
    },
    removeText() {
      this.text = null;
      localStorage.removeItem('info_message');
    }
  },
});
