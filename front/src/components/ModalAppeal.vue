<template>
  <div class="modal" :class="{ 'is-active': modalStore.modalWindowShow }">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="box">
        <div class="columns">
          <div class="column">
            <input v-model="name" type="text" class="input my-1" placeholder="Ваше имя" />
            <input v-model="contacts" type="tel" class="input my-1" placeholder="Номер телефона" />
            <button class="button is-rounded is-fullwidth my-1" @click="handleAppeal">Отправить</button>
            <p class="block is-size-7">
              При отправке формы даю согласие на хранение и обработку своих личных данных, указанных в данной контактной
              форме
            </p>
          </div>
          <div class="column">
            <textarea v-model="comment" type="textarea" class="input" placeholder="Комментарий к проекту"></textarea>
          </div>
        </div>
      </div>
    </div>
    <button class="modal-close is-large" aria-label="close" @click="modalStore.close()"></button>
  </div>
</template>
<script setup>
import axios from 'axios'
import { defineModel, ref } from 'vue'
import { useModalStore } from '@/stores/modal'
const baseURL = 'http://127.0.0.1:8000/api'
const modalStore = useModalStore()
const name = defineModel('name', { default: '' })
const contacts = defineModel('contacts')
// const is_valid_contacts = ref(true)
const is_valid_name = ref(true)
const comment = defineModel('comment')
async function handleAppeal() {
  //   is_valid_contacts.value = phonePattern.test(contacts.value)
  //   console.log(phonePattern)
  //   console.log(phonePattern.test(contacts.value))
  is_valid_name.value = !(name.value.trim().length === 0)
  if (is_valid_name.value) {
    const { response } = await axios.post(
      baseURL + '/appeal/',
      { name: name.value, phone: contacts.value, comment: comment.value },
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    )
  }
}
</script>
<style scoped>
input,
textarea {
  border-radius: 1rem;
}
textarea {
  height: 100%;
}
</style>
