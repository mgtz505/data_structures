//Implementation of a Stack

function Stack() {
    this.count = 0
    this.storage = {}

    this.push = (value) => {
        this.storage[this.count] = value
        this.count++
    }

    this.pop = () => {
        if(this.count === 0) {
            return undefined
        }
        this.count--
        let result = this.storage[this.count]
        delete this.storage[this.count]
        return result
    }

    this.peek = () => {
        return this.storage[this.count - 1]
    }

    this.size = () => {
        return this.count
    }
}



