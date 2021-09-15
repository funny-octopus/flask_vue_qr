var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        option:'category',
        items:null,
        add_item:'',
    },
    watch: {
        option:function(){
            var urll = '';
            switch(this.option){
                case 'category':
                    urll = '/api/category/';
                    break;
                case 'country':
                    urll = '/api/countries/';
                    break;
                case 'edizm':
                    urll = '/api/pricev/';
                    break;
            };
            axios.get(urll)
                .then(response => this.items = response.data.items);

        },
    },
    methods:{
        add:function(){
            if(this.add_item){
                this.items.push({'name':this.add_item,'article':'0','id':'0','count':'0'});
                this.add_item = '';
            }else{
                alert('Заполните сначала поле');
            };
        },
        remove:function(index){
            this.items.splice(index, 1);
        },
        save:function(){
            var urll = '';
            switch(this.option){
                case 'category':
                    urll = '/api/category/';
                    break;
                case 'country':
                    urll = '/api/countries/';
                    break;
                case 'edizm':
                    urll = '/api/pricev/';
                    break;
            };
            axios({
                method:'post',
                url:urll,
                data:this.items,
                headers:{
                    "Content-type":"application/json",
                },
            }).then(function(response){
                if(response.data.status==='ok'){
                    appp.items = appp.items.map(function(item){
                        item['count'] = '1';
                        return item;
                    });
                    alert('Успешно сохранено!');
                };
                if(response.data.status==='error'){
                    alert('Ошибка сохранения!');
                };
            }).catch(function(error){
                console.log(error);
            });
        },
    },
    created(){
        axios.get('/api/category/')
            .then(response => this.items = response.data.items);
    },

})
