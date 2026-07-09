<script setup lang="ts">


import type {AccordionItem} from '@nuxt/ui'

const items = ref<AccordionItem[]>([
  {
    label: 'Где находится питомник?',
    content: 'Наш питомник американских булли находится в Москве. Удобно добраться от станций метро «Румянцево» и «Солнцево».\n' +
        '\n' +
        'Посещение возможно по предварительной договорённости. На встрече вы познакомитесь со щенками, увидите их родителей, оцените условия содержания и получите ответы на вопросы о породе, выращивании, кормлении и воспитании щенка.\n' +
        '\n' +
        'Личное знакомство помогает выбрать щенка, который подойдёт именно вашей семье.'
  },
  {
    label: 'Как забронировать щенка?',
    content: 'Забронировать щенка можно по фото, видео или видеозвонку до его переезда в новый дом. Депозит составляет 30% от стоимости и закрепляет щенка за вами на весь период его роста в питомнике.\n' +
        '\n' +
        'Пока щенок находится у нас, вы наблюдаете за его развитием и характером в реальном времени.\n' +
        '\n' +
        'Личное посещение согласовывается заранее по звонку или сообщению. На встрече покажем условия содержания щенков и ответим на вопросы по выбору, документам и уходу.\n' +
        '\n' +
        'Депозит не возвращается: после его получения мы снимаем щенка с продажи и отказываем другим покупателям.'
  },
  {
    label: 'Как происходит доставка?',
    content: 'Доставляем щенков автомобильным, железнодорожным или авиационным транспортом. Работаем только с проверенными курьерскими службами.\n' +
        '\n' +
        'Стоимость доставки зависит от адреса и рассчитывается индивидуально. Расходы по доставке оплачивает покупатель.'
  },
  {
    label: 'Можно ли приехать в питомник?',
    content: 'До первой прививки щенки уязвимы к инфекциям, поэтому знакомство проходит по видеосвязи или через фото и видео.\n' +
        '\n' +
        'После первой прививки можно приехать в питомник и познакомиться со щенками лично по предварительной договорённости.'
  },
  {
    label: 'Когда можно забрать щенка домой?',
    content: 'Щенки готовы к переезду после первой прививки, в возрасте 8 недель.\n' +
        '\n' +
        'По желанию щенка можно оставить в питомнике до ревакцинации в 12 недель. К этому возрасту он получает полный комплект прививок и более устойчивый иммунитет, что облегчает адаптацию в новом доме.\n' +
        '\n' +
        'Более позднюю дату переезда согласовываем с заводчиком индивидуально.'
  },
  {
    label: 'Что заводчик не гарантирует?',
    content: 'Рост во взрослом возрасте прогнозируется по параметрам родителей и предыдущих пометов. Чем старше щенок, тем точнее прогноз, но итоговый размер зависит от индивидуального развития.\n' +
        '\n' +
        'Прикус может меняться до смены зубов. У булли допустим перекус, а щенки от родителей с прикусом "ножницы" имеют больше шансов на такое же смыкание. Точную оценку можно получить в 6-8 месяцев.\n' +
        '\n' +
        'Здоровье щенка на момент передачи гарантировано. После переезда в новую семью оно зависит от питания, физических нагрузок, своевременного лечения и условий содержания.\n' +
        '\n' +
        'Успех на выставках зависит от генетики, выращивания, обучения и работы с хендлером. Мы предоставляем щенков с хорошим выставочным потенциалом, а результат определяет дальнейшая подготовка.'
  },
])
import {stagger} from 'motion-v'
import {AnimatePresence, motion} from 'motion-v'

const gridVariants = {
  hidden: {},
  visible: {
    transition: {
      delayChildren: stagger(0.30),
      when: "beforeChildren",
    },
  },
}

const cardVariants = {
  hidden: {opacity: 0, y: 24, scale: 0.98, filter: "blur(4px)"},
  visible: {
    opacity: 1,
    y: 0,
    scale: 1,
    filter: "blur(0px)",
    transition: {duration: 0.7, ease: "easeOut"},
  },
}

const accordionAnimation = {
  initial: {
    height: 0,
    opacity: 0,
  },
  animate: {
    height: 'auto',
    opacity: 1,
  },
  exit: {
    height: 0,
    opacity: 0,
  },
  transition: {
    height: {
      duration: 0.3,
    },
    opacity: {
      duration: 0.2,
    },
  },
} as const

const {dogs: puppies} = useDogs('/puppies/')

const {dogs: producers} = useDogs('/producers/')

useSeoMeta({
  titleTemplate: '%s',
  title: 'Питомник американских булли BelovedBully в Москве - купить щенка',
  description: 'Щенки американского булли от титулованных родителей в питомнике BelovedBully (Москва). Фото, документы, доставка по России. Помогаем выбрать и бронируем щенка по видеосвязи.',
  ogTitle: 'Питомник американских булли BelovedBully - купить щенка',
  ogDescription: 'Щенки американского булли от титулованных родителей. Документы, доставка по России.',
  ogType: 'website',
})
</script>

<template>
  <HomeHero/>

  <UPageSection :ui="{ root: 'bg-elevated' }">
    <HomeDogsPreview
        title="Свободные щенки"
        subtitle="Найдите своего будущего друга"
        :dogs="puppies"
        fromContext="puppies"
        to="/puppies"
    />
  </UPageSection>

  <UPageSection class="bg-default" :ui="{container: 'flex flex-col lg:grid py-8 sm:py-8 lg:py-8 gap-8 sm:gap-16'}">
    <div class="flex flex-col items-left justify-left gap-2">
      <h2 class="text-3xl text-pretty tracking-tight text-highlighted font-serif">Как выбрать идеального щенка?</h2>
      <p class="sm:text-md text-toned">Выбирайте сердцем! Загляни в глаза своему будущему малышу. Почувствуй эту связь,
        эту искру! Сердце не обманет -
        оно выберет того самого!</p>
    </div>
  </UPageSection>

  <UPageSection :ui="{ root: 'bg-elevated' }">
    <HomeDogsPreview
        title="Наши производители"
        subtitle="Основа будущих поколений американских булли"
        :dogs="producers"
        fromContext="producers"
        to="/producers"
    />
  </UPageSection>

  <UPageSection class="bg-default">

    <div class="flex flex-col items-center justify-center gap-2">
      <h2 class="text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight text-highlighted font-serif">Частые
        вопросы</h2>
      <p class="sm:text-lg text-toned">Мы рады ответить на все ваши вопросы</p>
    </div>

    <UAccordion
        :items="items"
        :ui="{
      trigger: 'text-sm md:text-base',
      body: 'text-sm md:text-base'
    }"
    >
      <template #body="{ item, open }">
        <AnimatePresence :initial="false">
          <motion.div
              v-if="open"
              :key="item.label"
              class="overflow-hidden"
              v-bind="accordionAnimation"
          >
            {{ item.content }}
          </motion.div>
        </AnimatePresence>
      </template>
    </UAccordion>

  </UPageSection>

</template>

