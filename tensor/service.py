import tensorflow as tf
from tensor.model import Model

class Service(object):

    this = Model()

    @tf.function
    def plus(self):
        this = self.this
        return tf.add(this.num1, this.num2)

    @tf.function
    def minus(self):
        this = self.this
        return tf.subtract(this.num1, this.num2)

    @tf.function
    def multi(self):
        this = self.this
        return tf.multiply(this.num1, this.num2)

    @tf.function
    def plus(self):
        this = self.this
        return tf.div(this.num1, this.num2)
