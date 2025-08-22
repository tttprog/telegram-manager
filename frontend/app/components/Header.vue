<template>
  <div class="sticky top-0 mb-10">
    <u-container class="mt-5">
      <div
        class="flex items-center justify-between px-5 py-3 shadow-xl dark:shadow-gray-950 rounded-full backdrop-blur-xl z-50">
        <a href="/" class="flex items-center gap-3">
          <img src="/logo.png" alt="LOGO" class="w-12"></img>
          <h1 class="md:text-xl font-bold">Telegram Manager</h1>
        </a>
        <u-slideover class="lg:hidden" v-model:open="slideover">
          <u-button variant="soft" icon="solar:hamburger-menu-bold" size="xl" @click="slideover = true"></u-button>
          <template #content>
            <div class="self-end">
              <u-button variant="ghost" color="error" class="cursor-pointer" @click="slideover = false"
                icon="solar:close-circle-bold" size="xl"></u-button>
            </div>
            <div class="h-full m-4 flex flex-col justify-between w-full">
              <u-navigation-menu :items="menuItems" orientation="vertical"></u-navigation-menu>
              <div class="flex items-center gap-3 justify-between mx-5">
                <div class="flex items-center gap-1">
                  <u-button to="/accounts/login" @click="slideover = false" v-if="!authStore.isAuthenticated"
                    class="cursor-pointer" icon="solar:key-bold">Login</u-button>
                  <u-button to="/accounts/register" @click="slideover = false" v-if="!authStore.isAuthenticated"
                    class="cursor-pointer" icon="solar:user-plus-bold" color="neutral">Register</u-button>
                  <u-button @click="authStore.logout" v-if="authStore.isAuthenticated" class="cursor-pointer"
                    icon="solar:key-bold" color="error">Logout</u-button>
                </div>
                <u-button @click="changeColorMode" variant="ghost"
                  :icon="colorMode.value === 'dark' ? 'solar:moon-stars-linear' : 'solar:sun-linear'"
                  class="cursor-pointer"></u-button>
              </div>
            </div>
          </template>
        </u-slideover>

        <div class="items-center justify-between gap-10 hidden lg:flex">
          <!-- menu -->
          <u-navigation-menu :items="menuItems">
          </u-navigation-menu>
          <!-- menu -->
          <!-- color mode -->
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1">
              <u-button to="/accounts/login" @click="slideover = false" v-if="!authStore.isAuthenticated"
                class="cursor-pointer" icon="solar:key-bold">Login</u-button>
              <u-button to="/accounts/register" @click="slideover = false" v-if="!authStore.isAuthenticated"
                class="cursor-pointer" icon="solar:user-plus-bold" color="neutral">Register</u-button>
              <u-button @click="authStore.logout" v-if="authStore.isAuthenticated" class="cursor-pointer"
                icon="solar:key-bold" color="error">Logout</u-button>
            </div>
            <u-button @click="changeColorMode" variant="ghost"
              :icon="colorMode.value === 'dark' ? 'solar:moon-stars-linear' : 'solar:sun-linear'"
              class="cursor-pointer"></u-button>
          </div>
          <!-- color mode -->
        </div>
      </div>
    </u-container>
  </div>
</template>

<script lang="ts" setup>
import { useAuthStore } from '~/stores/auth'


const colorModeItems = ref(["light", "dark"])

const authStore = useAuthStore()

const slideover = ref(false)

const colorMode = useColorMode()

const changeColorMode = () => {
  colorMode.preference = colorMode.preference === 'dark' ? 'light' : 'dark'
}

const baseMenuItems = [
  {
    label: "Home",
    icon: "solar:home-2-bold",
    to: "/",
    onSelect: () => slideover.value = false,
  },
  {
    label: "About",
    icon: "solar:notebook-minimalistic-bold",
    to: "/about",
    onSelect: () => slideover.value = false,
  },
  {
    label: "Contact",
    icon: "solar:call-chat-bold",
    to: "/contact",
    onSelect: () => slideover.value = false,
  },
]

const menuItems = computed(() => {
  if (authStore.isAuthenticated) {
    return [
      ...baseMenuItems,
      {
        label: "Panel",
        icon: "solar:user-circle-bold",
        to: "/accounts/panel",
        onSelect: () => slideover.value = false,
      },
    ]
  } else {
    return [
      ...baseMenuItems,
    ]
  }
})

</script>

<style></style>