import DS from 'ember-data';

export default DS.Model.extend({
	name: DS.attr('string'),
	exercise: DS.hasMany('clientexercise', {async: true}),
	clientprofile: DS.belongsTo('clientprofile', {async: true}),


});
