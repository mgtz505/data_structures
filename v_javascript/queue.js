// Implementation of a Queue

function Queue() {
    let collection = []
    
    this.print = () => {
        console.log(collection)
    }

    this.enqueue = (element) => {
        collection.push(element)
    }

    this.dequeue = () => {
        return collection.shift()
    }

    this.front = () => {
        return collection[0]
    }

    this.isEmpty = () => {
        return collection.length === 0 // boolean
    }

    this.size = () => {
        return collection.length
    }
}