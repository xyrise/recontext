<script>
    let count = 0;

    function sum() {
        count++;
    }
</script>

<p>Counter: {count}</p>
<button class="ui button" on:click={sum}>Follow</button>

<style>
</style>
