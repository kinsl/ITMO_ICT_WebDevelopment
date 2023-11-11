import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore, useInfoStore } from '@/stores';
import { fetchWrapper } from '@/helpers';
import { DefaultLayout } from '@/layouts';
import { InfoView, SurveyView, LoginView } from '@/views';

const baseUrl = `${import.meta.env.VITE_API_URL}`;
let lastCheckFetchWasFrom = '';

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: DefaultLayout,
      props: {showTitle: true},
      children: [
        {
          path: '',
          name: 'Login',
          component: LoginView,
        },
      ],
    },
    {
      path: '/info',
      component: DefaultLayout,
      props: {showLogout: true},
      children: [
        {
          path: '',
          name: 'Info',
          component: InfoView,
        },
      ],
    },
    {
      path: '/survey',
      component: DefaultLayout,
      props: {showTitle: true, showGroupName: true, showLogout: true},
      children: [
        {
          path: '',
          name: 'Survey',
          component: SurveyView,
        },
      ],
    },
  ],
});


router.beforeEach(async (to) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const auth = useAuthStore();
  const info = useInfoStore();

  if (auth.access && (to.path !== '/survey' && to.path !== '/info')) {
    return {
      path: '/survey',
      query: to.query,
    };
  }

  else if (authRequired && !auth.access) {
    auth.returnUrl = to.fullPath;
    return {
      path: '/login',
      query: to.query,
    };
  }

  else if (to.path === '/survey') {
    try {
      const data = await fetchWrapper.get(`${baseUrl}/api/survey/user/check/`);
      lastCheckFetchWasFrom = '/survey';

      if (data.is_first_course !== true) {
        info.setText('Опрос только для первокурсников!');
        return { path: '/info' }
      } else if (data.is_faculty_active !== true) {
        info.setText('Опрос для вашего факультета ещё закрыт!');
        return { path: '/info' };
      } else if (data.has_adapters !== true) {
        info.setText('Не удалось получить информацию о ваших адаптерах!');
        return { path: '/info' };
      } else if (data.is_done === true) {
        info.setText('Опрос пройден!\nСпасибо 💙');
        return { path: '/info' };
      } else {
        info.removeText();
      }

    } catch(error) {
      info.setText('Ошибка при запросе информации для опроса');
      return { path: '/info' };
    }
  }

  else if (to.path === '/info') {
    if (lastCheckFetchWasFrom !== '/survey') {
      try {
        const data = await fetchWrapper.get(`${baseUrl}/api/survey/user/check/`);
        lastCheckFetchWasFrom = '/info';

        if (data.is_first_course !== true) {
          info.setText('Опрос только для первокурсников!');
        } else if (data.is_faculty_active !== true) {
          info.setText('Опрос для вашего факультета ещё закрыт!');
        } else if (data.has_adapters !== true) {
          info.setText('Не удалось получить информацию о ваших адаптерах!');
        } else if (data.is_done === true) {
          info.setText('Опрос пройден!\nСпасибо 💙');
        } else {
          info.removeText();
          return {path: '/survey'};
        }

      } catch (error) {
        info.setText('Ошибка при запросе информации для опроса');
      }
    }
  }
});
