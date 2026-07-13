// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: '2025-07-15',
    devtools: {enabled: false},
    modules: ['@nuxt/ui', 'motion-v/nuxt', '@nuxtjs/seo'],
    css: ['~/assets/css/main.css'],
    ui: {
        colorMode: false,
    },
    site: {
        url: 'https://belovedbully.ru',
        name: 'Питомник BelovedBully',
        description: 'Питомник американских булли BelovedBully в Москве - щенки от титулованных родителей, документы, доставка по России. Помогаем выбрать щенка и сопровождаем после переезда.',
        defaultLocale: 'ru',
    },

    vite: {
        server: {
            allowedHosts: ['belovedbully.ru', 'www.belovedbully.ru']
        }
    },

    fonts: {
        defaults: {
            weights: [400]
        },
        providers: {
            fontsource: false
        }
    },

    icon: {
        customCollections: [{
            prefix: 'custom',
            dir: './app/assets/icons'
        }]
    },

    runtimeConfig: {
        apiUrl: process.env.NUXT_API_URL ?? 'http://backend:8000/api/v1',
        public: {
            apiUrl: process.env.NUXT_PUBLIC_API_URL ?? '/api/v1'
        }
    },

    experimental: {
        viewTransition: true,
    },
})