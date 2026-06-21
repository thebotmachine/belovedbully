<script setup lang="ts">


import type {AccordionItem} from '@nuxt/ui'

const items = ref<AccordionItem[]>([
  {
    label: 'Где находится питомник?',
    content: 'Наш питомник американских булли находится в Москве. До нас удобно добраться от станций метро «Румянцево» и «Солнцево».\n' +
        '\n' +
        'Посещение питомника возможно по предварительной договорённости. Во время визита вы сможете познакомиться со щенками, увидеть их родителей, оценить условия содержания собак и получить ответы на вопросы о породе американский булли, выращивании щенка, кормлении и воспитании.\n' +
        '\n' +
        'Мы уделяем большое внимание здоровью, социализации и подбору будущих владельцев. Личное знакомство помогает вам принять взвешенное решение и выбрать щенка, который подойдёт именно вашей семье.'
  },
])
import {stagger} from 'motion-v'

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

const {dogs: puppies} = useDogs('/puppies/')

const {dogs: producers} = useDogs('/producers/')
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

  <UPageSection :ui="{container: 'flex flex-col lg:grid py-8 sm:py-8 lg:py-8 gap-8 sm:gap-16'}">
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
        subtitle="Которые гарантируют здоровье и красоту щенков"
        :dogs="producers"
        fromContext="producers"
        to="/producers"
    />
  </UPageSection>

  <UPageSection>
    <div class="flex flex-col items-center justify-center gap-2">
      <h2 class="text-3xl sm:text-4xl lg:text-5xl text-pretty tracking-tight text-highlighted font-serif">Частые
        вопросы</h2>
      <p class="sm:text-lg text-toned">Мы рады ответить на все ваши вопросы</p>
    </div>
    <UAccordion :items="items"/>

  </UPageSection>

</template>