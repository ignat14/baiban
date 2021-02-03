<template>
  <div>
    <h1>Spaces</h1>
    <SpacesList />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Spaces from '@/components/Spaces.vue';

@Options({
  components: {
    SpacesList: Spaces,
  },
})

export default class Home extends Vue {}
</script>
