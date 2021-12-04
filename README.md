# terminus: decentralized authorization

## Decentralizing authorization

### What is authorization?

Many programs have a concept of users. You log into these programs to identify yourself as a user of
their systems. This is their authentication layer.

Most programs that require you to identify yourself have an authorization layer. This layer is built
on top of the authentication layer, and represents which actions you are permitted to take on their
system.

On commercial programs, authorization is related to payments. Modern software services tend to have
three tiers of service - free, pro, and premium. Users on the free tier can only perform a limited
number of actions on these systems. Users on the pro tier can do everything that free users can do
plus a little bit extra. Users on the premium tier can do everything that pro users can do, plus a bit
extra.

For example, you need an Amazon account to order things from amazon.com. However, you can only access
their video streaming service if you are a member of Amazon Prime. Amazon's authorization layer is responsible
for telling the rest of Amazon's programs whether or not you are an Amazon Prime member. It is how
Amazon's streaming video service determines whether or not you are allowed to view the majority of
their videos for no additional cost.

Traditionally, authorization is represented in a centralized database and is totally under the control
of whoever is maintaining that database in production.

Going back to the Amazon example, Amazon is the final arbiter on whether or not you are a member of
Amazon Prime. They can revoke your authorization at any time without any explanation. You are completely
at their mercy. If you have paid for 1 year of Amazon Prime and decide in the middle of that year that
you no longer wish to be an Amazon Prime member, Amazon has all the power to decide how much they will
refund you. If you disagree with their decision, your only option is to take them to court.

`terminus` decentralizes the concept of authorization by representing a user's permissions for a system
as a token on a blockchain. If Amazon decided to use `terminus` as their authorization layer, as soon
as you decided that you no longer wished to be an Amazon Prime member, you could sell your membership
on an open market. You would still retain your Amazon user and be able to make regular purchases on
Amazon. The rights that go with an Amazon Prime membership would simply transfer to whoever purchased
your Amazon Prime membership token.

The ability to trade privileges on open markets is only one consequence of decentralizing authorization.
If you are a builder considering decentralized authorization for your application or a user considering
whether or not to use decentralized authorization for a service, there are a few things that you should
know going in:

### Authorization is not authentication

