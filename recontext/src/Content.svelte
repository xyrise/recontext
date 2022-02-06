<script>
    import ContentItem from './ContentItem.svelte';
    let articles = [
        {
            title:"Vaccine confidence in the time of COVID-19",
            sentences:"We call for a re-imagination of the culture of public health and the meaning of vaccine safety regulations. Public confidence in vaccination programs depends on the work they do for the community, rather than just the delivery of vaccine technology.",
            tags:["Community","Vaccine"],
            cited:6
        }
    ]
</script>

<div>
    {#each articles as article}
        <ContentItem title={article.title} 
        sentences={article.sentences} 
        tags={article.tags}
        cited={article.cited} />
    {/each}
</div>
