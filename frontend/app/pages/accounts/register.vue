<template>
  <div>
    <u-container>
      <div class="w-full flex items-center justify-between gap-10">
        <div class="w-1/2" v-if="$device.isDesktop">
          <img :src="$colorMode.value === 'dark' ? '/images/register-dark.png' : '/images/register.png'"
            class="lg:block rounded-4xl" alt="LOGIN IMAGE">
        </div>

        <UForm :schema="schema" :state="state" class="w-full lg:w-1/2 flex flex-col gap-3" @submit="onSubmit">
          <UFormField label="Email" name="email">
            <UInput v-model="state.email" class="w-full" size="xl" />
          </UFormField>

          <UFormField label="Password" name="password">
            <UInput v-model="state.password" type="password" class="w-full" size="xl" />
          </UFormField>
          <UFormField label="Password" name="password">
            <UInput v-model="state.password" type="password" class="w-full" size="xl" />
          </UFormField>
          <UButton type="submit" :loading="loading" class="justify-center w-full lg:w-1/4 cursor-pointer" size="xl">
            Register
          </UButton>
          <u-link class="self-end" :to="{ name: 'login' }">Alread have an account? Login</u-link>
        </UForm>
      </div>
    </u-container>
  </div>
</template>

<script lang="ts" setup>
definePageMeta({
  name: "register",
})

useSeoMeta({
  title: "Register",
})

import * as z from 'zod'
import type { FormSubmitEvent } from '@nuxt/ui'

const schema = z.object({
  email: z.string("Required").email('Invalid email'),
  password: z.string("Required").min(8, 'Must be at least 8 characters'),
  confirm: z.string("Required").min(8, 'Must be at least 8 characters'),
})

type Schema = z.output<typeof schema>

const state = reactive<Partial<Schema>>({
  email: undefined,
  password: undefined,
  confirm: undefined,
})

const toast = useToast()
const loading = ref(false)
async function onSubmit(event: FormSubmitEvent<Schema>) {
  loading.value = true
  toast.add({ title: 'Success', description: 'Login successfully.', color: 'success', icon: "solar:check-square-bold" })
  console.log(event.data)
  loading.value = false
}
</script>

<style></style>