<script>
    export let results;
    
    import ContentItem from './ContentItem.svelte';
    let articles = [];

    for(let i=0; i<3;i++){
        articles.push({
            title: results[i]['title'],
            sentences: (results[i]['abstract'].substring(0,140)+"...") ,
            tags:results[i]['keywords'],
            cited: results[i]['citationCount']
        })
    }
</script>

<div>
    {#each articles as article}
        <ContentItem title={article.title} 
        sentences={article.sentences} 
        tags={article.tags}
        cited={article.cited} />
    {/each}
</div>
