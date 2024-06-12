import { createApp } from 'vue'
import App from './App.vue'
import { createVuetify } from 'vuetify';
import { VApp, VMain, VContainer, VBtn } from 'vuetify/components';

const vuetify = createVuetify({
    components: {
        VApp,
        VMain,
        VContainer,
        VBtn,
    },
});

const app = createApp(App);
app.use(vuetify);
app.mount('#app');
