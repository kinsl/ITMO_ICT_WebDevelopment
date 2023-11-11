import { useAuthStore } from '@/stores';

const baseUrl = `${import.meta.env.VITE_API_URL}`;

export const fetchWrapper = {
  get: request('GET'),
  post: request('POST'),
  put: request('PUT'),
  delete: request('DELETE')
};

function request(method) {
  return async (url, body) => {
    const headers = await authHeader(url);
    const requestOptions = {
      method,
      headers,
    };
    if (body) {
      requestOptions.headers['Content-Type'] = 'application/json';
      requestOptions.body = JSON.stringify(body);
    }
    return fetch(url, requestOptions).then(handleResponse);
  }
}

async function refreshToken(refresh) {
  const authStore = useAuthStore();

  const response = await fetch(`${baseUrl}/oidc/token/refresh/`, {
    method: 'POST',
    body: JSON.stringify({ refresh: refresh }),
    headers: { 'Content-Type': 'application/json' },
  });

  if (!response.ok) {
    await authStore.logout();
  }

  const data = await response.json();

  if (data.access) {
    authStore.updateAccessToken(data.access, data.access_expiration);
  }

  return data.access;
}

async function checkAndRefreshToken() {
  const authStore = useAuthStore();
  const { access, access_expiration, refresh } = authStore;

  const expirationDate = new Date(access_expiration);
  const now = new Date();

  const isTokenExpired = now > expirationDate;

  if (isTokenExpired) {
    return refreshToken(refresh);
  }

  return access;
}

async function authHeader(url) {
  const authStore = useAuthStore();
  const isLoggedIn = !!authStore.access;
  const isApiUrl = url.startsWith(import.meta.env.VITE_API_URL);

  if (isLoggedIn && isApiUrl) {
    const access = await checkAndRefreshToken();
    return { Authorization: `Bearer ${access}` };
  } else {
    return {};
  }
}

async function handleResponse(response) {
  return response.text().then(async text => {
    const data = text && JSON.parse(text);

    if (!response.ok) {
      const authStore = useAuthStore();
      if ([401, 403].includes(response.status) && authStore.access) {
        await authStore.logout();
      }

      const error = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }

    return data;
  });
}
