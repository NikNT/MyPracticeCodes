<template>
  <h1>{{ name }}</h1>
  <p v-if="status === 'active'">User : Active</p>
  <p v-else-if="status === 'pending'">User : Pending</p>
  <p v-else>User : Inactive</p>

  <h3>
    <ul>
      <li v-for="task in tasks" :key="task">{{ task }}</li>
    </ul>
  </h3>
  <a :href="link" target="_blank">Link</a>
  <!-- <button v-on:click="toggleStatus">Toggle</button> -->
  <button @click="toggleStatus">Toggle</button>
</template>

<script>
export default {
  data() {
    return {
      name: "John Doe",
      status: "active",
      tasks: ["Task One", "Task Two", "Task Three"],
      link: "https://www.google.ca",
    };
  },
  methods: {
    toggleStatus() {
      if (this.status === "active") {
        this.status = "pending";
      } else if (this.status === "pending") {
        this.status = "inactive";
      } else {
        this.status = "active";
      }
    },
  },
};
</script>

<style scoped></style>
