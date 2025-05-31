from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.models import Schedule
from .. import db

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/')
def index():
    schedules = Schedule.get_all()
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
    return render_template('schedule/index.html', schedules=schedules, days=days)

@schedule_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        schedule = Schedule(
            day=request.form['day'],
            start_time=request.form['start_time'],
            end_time=request.form['end_time'],
            activity=request.form['activity'],
            description=request.form['description'],
            location=request.form['location']
        )
        schedule.save()
        flash('Aktivitas berhasil ditambahkan!', 'success')
        return redirect(url_for('schedule.index'))
    return render_template('schedule/add.html')

@schedule_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    schedule = Schedule.get_by_id(id)
    if not schedule:
        flash('Aktivitas tidak ditemukan!', 'error')
        return redirect(url_for('schedule.index'))
    
    if request.method == 'POST':
        schedule.day = request.form['day']
        schedule.start_time = request.form['start_time']
        schedule.end_time = request.form['end_time']
        schedule.activity = request.form['activity']
        schedule.description = request.form['description']
        schedule.location = request.form['location']
        schedule.save()
        flash('Aktivitas berhasil diperbarui!', 'success')
        return redirect(url_for('schedule.index'))
    
    return render_template('schedule/edit.html', schedule=schedule)

@schedule_bp.route('/delete/<int:id>')
def delete(id):
    schedule = Schedule.get_by_id(id)
    if schedule:
        schedule.delete()
        flash('Aktivitas berhasil dihapus!', 'success')
    else:
        flash('Aktivitas tidak ditemukan!', 'error')
    return redirect(url_for('schedule.index')) 