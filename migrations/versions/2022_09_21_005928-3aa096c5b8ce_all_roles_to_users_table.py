"""all roles to users table

Revision ID: 3aa096c5b8ce
Revises: 6830f901585d
Create Date: 2022-09-21 00:59:28.815778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa096c5b8ce'
down_revision = '6830f901585d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timezone', sa.Integer, nullable=True))
        batch_op.add_column(sa.Column('location', sa.VARCHAR(length=128), nullable=True))
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=24), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_status'), ['status'], unique=False)
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=24), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_role'), ['role'], unique=False)
        batch_op.create_foreign_key(batch_op.f('fk_user_tutor_id_user'), 'user', ['tutor_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_user_parent_id_user'), 'user', ['parent_id'], ['id'])
        batch_op.drop_column('username')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.VARCHAR(length=500), nullable=True))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_constraint('fk_user_tutor_id_user', type_='foreignkey')
        batch_op.drop_constraint('fk_user_parent_id_user', type_='foreignkey')

    # ### end Alembic commands ###
