<script setup lang="ts">
const route = useRoute()
const slug = computed(() => route.params.slug as string)

const {data: litter, pending, error} = useLitter(slug)

useSeoMeta({
  title: () => `${litter.value.name}`,
})

const {formatDate, formatAge} = useFormatDate()

const breadcrumbItems = useBreadcrumbItems({
  overrides: [
    undefined,
    undefined,
    {
      label: computed(() => litter.value?.name || slug.value),
    }
  ]
})



</script>

<template>
  <div class="bg-elevated">
    <UContainer class="py-8">
      <UBreadcrumb :items="breadcrumbItems" class="mb-8"/>

      <div v-if="pending">Загрузка...</div>

      <div v-else-if="error">Не удалось загрузить собаку.</div>

      <div v-else-if="litter"
           class="bg-default border-b-3 border-accented ring-1 ring-accented/40 shadow-lg rounded-xl p-4">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <div class="relative aspect-square overflow-hidden bg-muted rounded-lg">
            <img
                v-if="litter.medium_url"
                :src="litter.medium_url"
                alt="Product illustration"
                loading="lazy"
                class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
            />
            <div class="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
          </div>

          <div class="space-y-4">

              <h1 class="text-5xl leading-tight font-medium text-balance font-serif">{{ litter.name }}</h1>
              <div class="flex flex-wrap items-center gap-2 text-toned">
                <UBadge color="neutral" variant="outline">{{ litter.puppies_count }} щенков</UBadge>
                <div>
                  <UBadge color="neutral" variant="outline">Есть свободные щенки</UBadge>
                </div>
                <UBadge color="neutral" variant="outline">Заглушка</UBadge>
              </div>
              <p class="max-w-prose text-muted leading-relaxed ">{{ litter.description }}</p>


            <div class="bg-muted rounded-xl p-4 leading-relaxed space-y-2">
              <div class="flex justify-between">
                <div class="text-muted">Дата рождения</div>
                <div class="font-medium">{{ formatDate(litter.birth_date) }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Количество щенков</div>
                <div class="font-medium">{{ litter.puppies_count }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Мальчиков</div>
                <div class="font-medium">{{ litter.males_count }}</div>
              </div>

              <USeparator :ui="{ border: 'border-accented' }"/>

              <div class="flex justify-between">
                <div class="text-muted">Девочек</div>
                <div class="font-medium">{{ litter.females_count }}</div>
              </div>

              <div class="bg-elevated rounded-xl p-4 space-y-2 -mx-4 -mb-4">
                <div class="flex justify-between">
                  <div class="text-muted">Мама помёта</div>
                  <ULink
                      :to="`/dogs/${litter.mother.slug}`"
                      raw
                      class="group font-medium flex items-center gap-1 hover:text-neutral-700 transition-colors"
                  >
                    {{ litter.mother.name }}
                    <UIcon
                        name="i-lucide-chevron-right"
                        class="size-4 transition-transform duration-300 group-hover:translate-x-1"
                    />
                  </ULink>
                </div>

                <USeparator :ui="{ border: 'border-accented' }"/>

                <div class="flex justify-between">
                  <div class="text-muted">Папа помёта</div>
                  <ULink
                      :to="`/dogs/${litter.father.slug}`"
                      raw
                      class="group font-medium flex items-center gap-1 hover:text-neutral-700 transition-colors"
                  >
                    {{ litter.father.name }}
                    <UIcon
                        name="i-lucide-chevron-right"
                        class="size-4 transition-transform duration-300 group-hover:translate-x-1"
                    />
                  </ULink>
                </div>


              </div>


            </div>
          </div>

        </div>

        <div class="">
          <div class="text-center py-8 text-4xl leading-tight font-medium text-balance font-serif">Потомство<span class="text-base md:text-lg align-top text-neutral-300 italic">({{ litter.puppies_count }})</span>
          </div>
          <DogsGrid :dogs="litter.puppies" from-context="litters"/>
        </div>

      </div>
    </UContainer>
  </div>
</template>
