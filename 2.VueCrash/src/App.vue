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
</template>

<script>
export default {
  data() {
    return {
      name: "John Doe",
      status: "active",
      tasks: ["Task One", "Task Two", "Task Three"],
    };
  },
};
</script>

<style scoped></style>
