import {
    createRouter,
    createWebHistory
} from 'vue-router';

import home from '../views/home.vue';
import New from '../views/new.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: home
    },
    {
        path: '/new',
        name: 'new',
        component: New
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
