<script setup lang="ts">

</script>

<template>
 <div class="border-t-2 border-accented">
    <footer class="mx-auto flex max-w-7xl flex-col items-center gap-4 px-4 py-6">
      <Logo class="h-36 text-muted"/>
      <span class="text-center text-sm text-muted">
        © {{ new Date().getFullYear() }}, <ULink to="https://belovedbully.ru/">BelovedBully</ULink> - Все права защищены.
      </span>
    </footer>
  </div>
</template>
