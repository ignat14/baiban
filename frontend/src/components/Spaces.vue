<template>
  <div>
    <ul v-for="space in spaces" :key="space.id">
      <li>
        <span>{{ space.name }}</span>
        <img :src="space.avatar" width="150" />
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import axios from 'axios';

@Options({
  props: {
    msg: String
  }
})
export default class Spaces extends Vue {
  msg!: string
  spaces: object[] = []

  async created() {
    const response = await axios.get('api/v1/space/space/')
    this.spaces = response.data

  }
}
</script>

<style scoped lang="scss">
li {
  display: flex;
  justify-content: center;
  align-items: center;

  & > * {
    margin: 10px;
  }
}
</style>
