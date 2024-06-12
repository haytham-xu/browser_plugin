<template>
  <v-app>
    <v-main>
      <v-container>
        <v-btn color="primary" @click="getTabsAndSend">Get Tabs Url</v-btn>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  methods: {
    getTabsAndSend() {
      chrome.tabs.query({}, tabs => {
        const urls = tabs.map(tab => tab.url);
        axios.post('http://127.0.0.1:5000/tabs', { tabs: urls })
          .then(response => {
            console.log(response.data);
          })
          .catch(error => {
            console.error(error);
          });
      });
    }
  }
}
</script>

<style>
  body {
    width: 348px;
    height: 600px;
  }
</style>
