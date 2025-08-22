<template>
  <div>
    <u-container>
      <div class="w-full flex items-center justify-between gap-10">
        <div class="w-1/2" v-if="$device.isDesktop">
          <img :src="$colorMode.value === 'dark' ? '/images/login-dark.png' : '/images/login.png'"
            class="lg:block rounded-4xl" alt="LOGIN IMAGE">
        </div>

        <UForm :schema="schema" :state="state" class="w-full lg:w-1/2 flex flex-col gap-3" @submit="onSubmit">
          <UFormField label="Email" name="email">
            <UInput v-model="state.email" class="w-full" size="xl" />
          </UFormField>

          <UFormField label="Password" name="password">
            <UInput v-model="state.password" type="password" class="w-full" size="xl" />
          </UFormField>
          <div class="flex items-center justify-between w-full">
            <UFormField label="Remember Me" name="remember" class="flex items-center gap-3">
              <UCheckbox v-model="state.remember" type="checkbox" class="w-full" size="xl" />
            </UFormField>
            <u-link :to="{ name: 'forgotpassword' }">Forgot password?</u-link>
          </div>
          <UButton type="submit" :loading="loading" class="justify-center w-full lg:w-1/4 cursor-pointer" size="xl">
            Login
          </UButton>
          <u-link class="self-end" :to="{ name: 'register' }">Do not have an account?</u-link>
        </UForm>

      </div>
    </u-container>
  </div>
</template>

<script lang="ts" setup>
definePageMeta({
  name: 'login',
})

useSeoMeta({
  title: "Login",
})

import * as z from 'zod'
import type { FormSubmitEvent } from '@nuxt/ui'
import { UCheckbox } from '#components'

const schema = z.object({
  email: z.string("Required").email('Invalid email'),
  password: z.string("Required").min(8, 'Must be at least 8 characters'),
  remember: z.boolean()
})

type Schema = z.output<typeof schema>

const state = reactive<Partial<Schema>>({
  email: undefined,
  password: undefined,
  remember: true,
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