var application = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        collections:[],
    },
    methods:{
        get_collections:function(){
            factory = document.getElementById('factory').value;
            console.log(factory);
            axios.get('/api/collections/'+factory)
               .then(response => this.collections = response.data.items);
        },
    },
})

