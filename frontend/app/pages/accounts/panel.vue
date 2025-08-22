<template>
  <div>
    panel
  </div>
</template>

<script lang="ts" setup>
definePageMeta({
  middleware: "auth"
})

useSeoMeta({
  title: "Panel"
})
</script>

<style></style>