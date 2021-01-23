<template>
  <div class="home">
    <Spaces />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Spaces from '@/components/Spaces.vue'; // @ is an alias to /src

@Options({
  components: {
    Spaces,
  },
})
export default class Home extends Vue {}
</script>
